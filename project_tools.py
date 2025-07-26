# project_tools.py

import os

def auto_dev(project_name):
    brain_path = f"projects/{project_name}/project_brain.md"
    todo_path = f"projects/{project_name}/todo.md"

    if not os.path.exists(brain_path):
        print(f"❌ No project brain found for {project_name}")
        return

    with open(brain_path, "r") as f:
        idea = f.read()

    # Simple roadmap breakdown from idea
    tasks = []

    if "Markdown" in idea:
        tasks.append("- [ ] Add Markdown parser to backend")
    if "dark mode" in idea.lower():
        tasks.append("- [ ] Implement dark/light theme toggle in UI")
    if "post filtering" in idea.lower():
        tasks.append("- [ ] Build UI for filtering posts by tags/date")
    tasks += [
        "- [ ] Design homepage layout",
        "- [ ] Add post editor interface",
        "- [ ] Add save/load functionality",
        "- [ ] Connect frontend with backend",
        "- [ ] Add deployment script (GitHub Pages / Vercel)"
    ]

    with open(todo_path, "a") as f:
        f.write("\n## 🚀 Dev Roadmap\n")
        for task in tasks:
            f.write(task + "\n")

    print(f"✅ Development roadmap added to {todo_path}")
