# School Lunch Menu

A Python/Flask web application for managing and displaying school lunch menus.

## Requirements

- Python 3.12+
- Flask

## Getting Started

### Option 1: VSCode Dev Container (Recommended)

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and the [VSCode Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
2. Open this folder in VSCode.
3. When prompted, click **Reopen in Container** (or run the command `Dev Containers: Reopen in Container`).
4. Once the container is ready, press **F5** to launch the app in debug mode.
5. Open your browser to [http://localhost:5000](http://localhost:5000).

### Option 2: Local Development

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask run --debug
```

Then open [http://localhost:5000](http://localhost:5000).

## Project Structure

```
.
├── .devcontainer/        # VSCode Dev Container configuration
├── .vscode/              # VSCode editor settings and launch configs
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
└── README.md             # This file
```
