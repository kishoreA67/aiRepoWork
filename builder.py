# builder.py

import os
from datetime import datetime

def create_project(name, template="basic"):
    root = f"projects/{name}"
    os.makedirs(root, exist_ok=True)

    with open(f"{root}/README.md", "w") as f:
        f.write(f"# {name}\n\nCreated by AmanAI on {datetime.now().strftime('%Y-%m-%d')}.\n")

    if template == "basic":
        with open(f"{root}/main.py", "w") as f:
            f.write(f'print("👋 This is {name}")\n')

    elif template == "html-css":
        with open(f"{root}/index.html", "w") as f:
            f.write("<!DOCTYPE html>\n<html>\n<head><title>New Project</title></head>\n<body>\n</body>\n</html>")
        with open(f"{root}/style.css", "w") as f:
            f.write("/* Styles */")

    elif template == "cli":
        with open(f"{root}/cli.py", "w") as f:
            f.write('''import sys\nprint("🔧 CLI running:", sys.argv[1:])''')

    print(f"✅ Created project '{name}' with template: {template}")
