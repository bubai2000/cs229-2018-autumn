import os

BASE_DIR = "problem-sets"   # change if needed


def generate_index(dir_path, root_path):
    items = sorted(os.listdir(dir_path))

    rel_path = os.path.relpath(dir_path, root_path)

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Index of {rel_path}</title>
    <style>
        body {{ font-family: Arial; padding: 20px; }}
        h2 {{ border-bottom: 1px solid #ccc; }}
        ul {{ list-style-type: none; padding-left: 0; }}
        li {{ margin: 6px 0; }}
        a {{ text-decoration: none; color: #0366d6; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>

<h2>📁 Index of {rel_path}</h2>
<ul>
"""

    # Back link
    if dir_path != root_path:
        html += '<li><a href="../">⬅️ Parent Directory</a></li>\n'

    for item in items:
        if item == "index.html":
            continue

        full_path = os.path.join(dir_path, item)

        if os.path.isdir(full_path):
            html += f'<li>📁 <a href="{item}/">{item}/</a></li>\n'
        else:
            html += f'<li>📄 <a href="{item}">{item}</a></li>\n'

    html += """
</ul>
</body>
</html>
"""

    with open(os.path.join(dir_path, "index.html"), "w") as f:
        f.write(html)

    # Recurse into subdirectories
    for item in items:
        full_path = os.path.join(dir_path, item)
        if os.path.isdir(full_path):
            generate_index(full_path, root_path)


if __name__ == "__main__":
    generate_index(BASE_DIR, BASE_DIR)
    print("✅ Directory indexes generated!")
