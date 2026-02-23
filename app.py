import json
import os
from datetime import datetime, timedelta

from flask import Flask, jsonify, redirect, render_template, request, url_for
import requests as http_requests

app = Flask(__name__)

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.json")

DEFAULT_CONFIG = {
    "school_id":    "d7bd7613-a7ac-4508-b50f-fd713b8b9bba",
    "serving_line": "Main (Trayline)",
    "meal_type":    "Lunch",
    "grade":        "01",
}

# Hardcoded – PersonId is not meaningful for anonymous access
PERSON_ID = "00000000-0000-0000-0000-000000000000"

API_URL = (
    "https://webapis.schoolcafe.com/api/CalendarView/GetDailyMenuitemsByGrade"
)

GRADE_OPTIONS = {
    "Elementary": [
        ("K",  "Kindergarten (K)"),
        ("01", "Grade 1"),
        ("02", "Grade 2"),
        ("03", "Grade 3"),
        ("04", "Grade 4"),
        ("05", "Grade 5"),
    ],
    "Middle": [
        ("06", "Grade 6"),
        ("07", "Grade 7"),
        ("08", "Grade 8"),
    ],
    "High": [
        ("09", "Grade 9"),
        ("10", "Grade 10"),
        ("11", "Grade 11"),
        ("12", "Grade 12"),
    ],
}

SCHOOL_OPTIONS = [
    ("d7bd7613-a7ac-4508-b50f-fd713b8b9bba", "Miller Elementary", "Elementary"),
]

SERVING_LINE_MAP = {
    "Breakfast": "Hot Breakfast",
    "Lunch":     "Main (Trayline)",
}


# ── Config helpers ────────────────────────────────────────────────────────────

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return DEFAULT_CONFIG.copy()


def save_config(cfg):
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=2)


# ── Week helpers ──────────────────────────────────────────────────────────────

def get_week(offset: int):
    """Return (sunday, saturday) for the week at `offset` weeks from today."""
    today = datetime.now().date()
    # Python weekday(): Mon=0 … Sun=6  →  days since Sunday = (weekday+1) % 7
    days_since_sunday = (today.weekday() + 1) % 7
    sunday = today - timedelta(days=days_since_sunday) + timedelta(weeks=offset)
    saturday = sunday + timedelta(days=6)
    return sunday, saturday


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    try:
        offset = int(request.args.get("offset", 0))
    except ValueError:
        offset = 0
    offset = max(-4, min(4, offset))

    sunday, saturday = get_week(offset)
    today = datetime.now().date()

    weekdays = []
    for i in range(1, 6):          # 1 = Monday … 5 = Friday
        d = sunday + timedelta(days=i)
        weekdays.append({
            "name":     d.strftime("%A"),
            "label":    f"{d.strftime('%b')} {d.day}",
            "api_date": d.strftime("%m/%d/%Y"),
            "iso":      d.strftime("%Y-%m-%d"),
            "is_today": d == today,
        })

    week_label = (
        f"{sunday.strftime('%b')} {sunday.day}"
        f" \u2013 "
        f"{saturday.strftime('%b')} {saturday.day}, {saturday.year}"
    )

    return render_template(
        "index.html",
        weekdays=weekdays,
        offset=offset,
        week_label=week_label,
        can_go_back=offset > -4,
        can_go_forward=offset < 4,
    )


@app.route("/api/menu")
def api_menu():
    date_str = request.args.get("date")
    if not date_str:
        return jsonify({"error": "date parameter required"}), 400

    cfg = load_config()
    params = {
        "SchoolId":    cfg["school_id"],
        "ServingDate": date_str,
        "ServingLine": cfg["serving_line"],
        "MealType":    cfg["meal_type"],
        "Grade":       cfg["grade"],
        "PersonId":    PERSON_ID,
    }

    try:
        resp = http_requests.get(API_URL, params=params, timeout=10)
        resp.raise_for_status()
        return jsonify(resp.json())
    except http_requests.RequestException as e:
        return jsonify({"error": str(e)}), 502


@app.route("/settings", methods=["GET", "POST"])
def settings():
    cfg = load_config()

    if request.method == "POST":
        cfg["school_id"]    = request.form.get("school_id", "").strip()
        cfg["meal_type"]    = request.form.get("meal_type", "").strip()
        cfg["serving_line"] = SERVING_LINE_MAP.get(cfg["meal_type"], "Main (Trayline)")
        cfg["grade"]        = request.form.get("grade",     "").strip()
        save_config(cfg)
        return redirect(url_for("index"))

    current_school_type = next(
        (t for sid, _name, t in SCHOOL_OPTIONS if sid == cfg["school_id"]),
        "Elementary",
    )
    return render_template(
        "settings.html",
        config=cfg,
        grade_options=GRADE_OPTIONS[current_school_type],
        grade_options_by_type=GRADE_OPTIONS,
        school_options=SCHOOL_OPTIONS,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
