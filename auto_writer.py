# auto_writer.py
import os
from datetime import datetime
from brain import store_thought

def auto_write(project):
    base_path = f"projects/{project}"
    brain_file = os.path.join(base_path, "project_brain.md")
    notes_file = os.path.join(base_path, "notes.md")
    output_file = os.path.join(base_path, "code", "article.md")

    if not os.path.exists(brain_file) or not os.path.exists(notes_file):
        print("❌ Missing project_brain.md or notes.md.")
        return

    with open(brain_file, "r") as f1, open(notes_file, "r") as f2:
        brain = f1.read()
        notes = f2.read()

    # Combine and generate content
    title = f"# Blog: {project.replace('-', ' ').title()}\n"
    intro = "This article explores the core ideas behind this project.\n\n"
    article_body = f"## Idea\n{brain}\n\n## Notes\n{notes}\n\n## Summary\nThis blog explained the main design and learning points."

    full_content = title + intro + article_body

    os.makedirs(os.path.join(base_path, "code"), exist_ok=True)
    with open(output_file, "w") as f:
        f.write(full_content)

    print(f"📝 Blog written to: {output_file}")
    store_thought("Auto-Written Blog", f"Generated blog for {project} using brain + notes.")
