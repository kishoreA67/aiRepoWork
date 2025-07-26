# publish.py

import os
import subprocess
from datetime import datetime

def publish():
    message = f"📤 Auto-publish {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"✅ Pushed to GitHub with message: {message}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")

    with open("publish_log.md", "a") as f:
        f.write(f"\n- {message}")

