# project_brain.py

import os
from datetime import datetime

def project_brain(project, idea=None):
    folder = f"projects/{project}"
    path = os.path.join(folder, "project_brain.md")

    if not os.path.exists(folder):
        print(f"❌ Project '{project}' not found.")
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    header = f"\n## 🧠 {project} Thought ({now})\n"

    if idea:
        content = f"{header}{idea}\n" + "-"*40 + "\n"
        with open(path, "a") as f:
            f.write(content)
        print(f"🧠 Thought saved in {path}")
    else:
        if os.path.exists(path):
            with open(path, "r") as f:
                print(f.read())
        else:
            print("🤖 No project thoughts yet.")
