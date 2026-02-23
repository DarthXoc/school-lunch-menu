# School Lunch Menu

A Python/Flask web app that fetches and displays your school's daily lunch (or breakfast) menu from the SchoolCafe API, organized in a weekly calendar view.

## Features

- Weekly calendar view with prev/next navigation
- Fetches live menu data from the SchoolCafe API
- Configurable school, grade, and meal type via a Settings page
- Meal type and serving line dynamically fetched from the SchoolCafe API based on the selected school
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
| School District | Dropdown of supported districts; changing it reloads the school list |
| School | Schools fetched from the SchoolCafe API for the selected district |
| Grade | Grades scoped to the selected school type (Elementary, Middle, High) |
| Meal Type | Populated from the API for the selected school |
| Serving Line | Populated from the API based on the selected school and meal type |

Settings are saved to `config.json` in the project root (git-ignored). If the file doesn't exist, defaults are used.

## Adding a District

In `app.py`, add an entry to `DISTRICT_OPTIONS`:

```python
DISTRICT_OPTIONS = [
    ("4585", "Celina ISD"),
    ("1611", "Frisco ISD"),
    ("<district_id>", "My District"),
]
```

The district ID can be found by inspecting SchoolCafe API traffic for your district. Once added, selecting the district in Settings will automatically fetch its school list from the API.

## License

MIT License — see below.

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

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
