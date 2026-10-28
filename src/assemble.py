# -*- coding: utf-8 -*-
"""
assemble.py
Combines CSS, HTML, and JS with embedded Base64 imagery into a single standalone HTML file.
"""

import os, base64, json
from v3_css import CSS
from v3_html import get_html
from v3_js import JS

src_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(src_dir, ".."))
proc_dir = os.path.join(src_dir, "assets")

assets = {
    "saturn": "saturn.jpg",
    "mercury": "mercury.jpg",
    "venus": "venus.jpg",
    "earth": "earth.jpg",
    "mars": "mars.jpg",
    "jupiter": "jupiter.jpg",
    "uranus": "uranus.jpg",
    "neptune": "neptune.jpg",
    "titan": "titan.jpg",
    "io": "io.jpg",
    "moon": "moon.jpg",
    "europa": "europa.jpg",
    "enceladus": "enceladus.jpg",
    "cliffs": "cliffs.jpg",
    "galaxy": "galaxy.jpg",
    "blackhole": "m87_blackhole.jpg",
    "trappist": "trappist1.jpg",
    "voyager": "voyager.jpg"
}

b64 = {}
for k, fname in assets.items():
    p = os.path.join(proc_dir, fname)
    with open(p, "rb") as f:
        b64[k] = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")

print(f"Base64 encoded {len(b64)} assets.")

# Inject base64 dictionary to global JS namespace for dynamic switching
b64_js = "window.b64Assets = " + json.dumps(b64) + ";\n" + JS

# Generate HTML markup
html_content = get_html(b64)

# Replace placeholders
html_content = html_content.replace("/* CSS will be injected here */", CSS)
html_content = html_content.replace("/* JS logic will be injected here */", b64_js)

targets = [
    os.path.join(root_dir, "outputs", "远处-宇宙观察笔记.html"),
    os.path.join(root_dir, "index.html")
]

for t in targets:
    os.makedirs(os.path.dirname(t), exist_ok=True)
    with open(t, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully generated: {t} ({os.path.getsize(t)} bytes)")
