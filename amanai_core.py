# amanai_core.py

from datetime import datetime
import os
import subprocess

def train():
    print("🧠 Training from current project files...")
    # Here you can add parsing of code, analysis, etc.
    files = os.listdir(".")
    print(f"🔍 Found {len(files)} files: {files}")
    print("✅ Basic scan complete. (Extend me!)")

def log_day():
    log_file = "amanai_log.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"## Log Entry – {timestamp}\n- Trained on current project files\n- Updated brain modules\n\n"
    with open(log_file, "a") as f:
        f.write(entry)
    print(f"📓 Log entry written to `{log_file}`")

def push():
    print("🚀 Committing log and updates to GitHub...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "📓 Daily log + training update"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Successfully pushed to GitHub.")
    except subprocess.CalledProcessError:
        print("❌ Git commit or push failed.")
