import sys
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

print("** app.py loaded — Flask app created **", flush=True)


@app.route("/")
def index():
    print(f"** GET / — request from {request.remote_addr} **", flush=True)
    python_version = sys.version
    current_time = datetime.now().strftime("%A, %B %d, %Y at %I:%M:%S %p")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>School Lunch Menu</title>
    <style>
        body {{
            font-family: system-ui, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: #f0f4f8;
        }}
        .card {{
            background: white;
            border-radius: 12px;
            padding: 2.5rem 3rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            text-align: center;
            max-width: 480px;
        }}
        .badge {{
            display: inline-block;
            background: #22c55e;
            color: white;
            border-radius: 999px;
            padding: 0.25rem 0.9rem;
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 1.25rem;
        }}
        h1 {{
            margin: 0 0 0.5rem;
            font-size: 1.75rem;
            color: #1e293b;
        }}
        p {{
            color: #64748b;
            margin: 0.4rem 0;
            font-size: 0.95rem;
        }}
        .meta {{
            margin-top: 1.75rem;
            padding-top: 1.25rem;
            border-top: 1px solid #e2e8f0;
            font-size: 0.8rem;
            color: #94a3b8;
        }}
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">&#10003; Running</div>
        <h1>School Lunch Menu</h1>
        <p>Flask is up and Python is running.</p>
        <div class="meta">
            <p><strong>Python</strong> {python_version}</p>
            <p><strong>Time</strong> {current_time}</p>
        </div>
    </div>
</body>
</html>"""


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
