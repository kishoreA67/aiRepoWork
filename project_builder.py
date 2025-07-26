import os
from datetime import datetime

def build_project(name, domain="general"):
    path = f"projects/{name}"
    os.makedirs(path, exist_ok=True)

    readme_path = os.path.join(path, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# {name}\n\n")
        f.write(f"- Created: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"- Domain: {domain}\n")
        f.write(f"- Goal: TODO - Describe project goal\n")

    print(f"✅ Project '{name}' created at {path}")
